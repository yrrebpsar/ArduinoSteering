import Part
import PartGui
import Draft

doc = App.ActiveDocument
gui = Gui.ActiveDocument
m = doc.getObjectsByLabel("M")[0];

def alias():
    for row in range(2, 100):
        for col in range(ord('B'), ord('Z')):
            cellPrefix = chr(col)+'1';
            cellPostfix = 'A'+str(row);
            
            prefix = m.getContents(cellPrefix);
            postfix = m.getContents(cellPostfix);
            if prefix == '' or postfix=='':
                continue
                
            label = prefix+postfix;
            cell = chr(col)+str(row);
            currentalias = m.getAlias(cell);
            print label;
            m.setAlias(cell, label);
            if m.getContents(cell) == '':
                m.set(cell, '0mm')
                if prefix == 'x':
                    m.set(cell, '=-0.5*l' + postfix)
                if prefix == 'y':
                    m.set(cell, '=-0.5*w' + postfix)
                if prefix == 'z':
                    m.set(cell, '=-0.5*h' + postfix)
                if prefix.startswith('angle'):
                    m.set(cell, '0deg')


def link(obj, prop):
    dict = { 
        'r': 'Radius',
        'l': 'Length',
        'w': 'Width',
        'h': 'Height',
        'x': 'Placement.Base.x',
        'y': 'Placement.Base.y',
        'z': 'Placement.Base.z'
    }

    for p in prop:
        alias = "M."+p+obj.Name;
        try:
            obj.setExpression(dict[p], alias)
        except:
            print 'No Property ' + dict[p] + ' on ' + obj.Name

def create(type, name):
    if doc.getObject(name):
        doc.removeObject(name);
    result = doc.addObject(type, name)
    return result

def value(alias):
    return m.get(m.getCellFromAlias(alias))

def createAll(name):
    result = create(value('t'+name), name)
    link(result, ['x', 'y', 'z', 'l', 'w', 'h', 'r'])
    rotate(result, 'x', value('angleX'+name))
    rotate(result, 'y', value('angleY'+name))
    rotate(result, 'z', value('angleZ'+name))
    return result

def cut(name, base, tool):
    result = create("Part::Cut", name)
    result.Base = base
    result.Tool = tool
    base.ViewObject.hide()
    tool.ViewObject.hide()
    return result

def combine(name, objects):
    result = create('Part::MultiFuse', name)
    result.Shapes = objects
    for o in objects:
        guiObject = gui.getObject(o.Name)
        guiObject.hide()
    return result


def extrude(name, obj):
    alias = 'M.h'+name
    result = create('Part::Extrusion', name)
    link(result, {'x', 'y', 'z'})
    result.Base = obj
    result.Solid = True
    result.setExpression('LengthFwd', alias)
    result.Base.ViewObject.hide()
    return result

def rotate(obj, axis, angle): 
    axes = {
        'x': App.Vector(1,0,0),
        'y': App.Vector(0,1,0),
        'z': App.Vector(0,0,1)
    }
    obj.Placement = App.Placement(
        App.Vector(0,0,0),
        App.Rotation(axes[axis], angle), 
        App.Vector(0,0,0)).multiply(obj.Placement)

doc.recompute()
