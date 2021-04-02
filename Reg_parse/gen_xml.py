import xml.etree.ElementTree as ET
import xml.dom.minidom as Dom  


NS = {"default": {"ns":"ipxact", "uri":"http://www.accellera.org/XMLSchema/IPXACT/2.0"},
      "vendor":{"ns":"armchina", "uri":"www.armchina.com"},
      "xsi":{"ns":"xsi", "uri":"http://www.w3.org/2001/XMLSchema-instance"}}

schemaLocation = "http://www.accellera.org/XMLSchema/IPXACT/2.0/index.xsd"
 
doc = Dom.Document()  

def ns_name(ns,name):
    if ns not in NS:
        raise Exception("namespce not exist")
    ns_def=NS["default"]["ns"]
    if ns_def!="":
       return ns_def+":"+name
    else:
       return name

# fill field information
def fill_field_info(field,father_node):
    newel = doc.createElement(ns_name("default","name"))
    newtext = doc.createTextNode(field.name)
    newel.appendChild(newtext)
    father_node.appendChild(newel)

    newel = doc.createElement(ns_name("default","displayName"))
    newtext = doc.createTextNode(field.full_name)
    newel.appendChild(newtext)
    father_node.appendChild(newel)

    if field.full_name == 'Reserved': 
        newel = doc.createElement(ns_name("default","reserved"))
        newtext = doc.createTextNode('true')
        newel.appendChild(newtext)
        father_node.appendChild(newel)


    newel = doc.createElement(ns_name("default","description"))
    newtext = doc.createTextNode(field.description)
    newel.appendChild(newtext)
    father_node.appendChild(newel)

    if field.volatile == 'true': 
        newel = doc.createElement(ns_name("default","volatile"))
        newtext = doc.createTextNode(field.volatile)
        newel.appendChild(newtext)
        father_node.appendChild(newel)

    newel = doc.createElement(ns_name("default","bitOffset"))
    newtext = doc.createTextNode(str(field.lsb))
    newel.appendChild(newtext)
    father_node.appendChild(newel)

    newel = doc.createElement(ns_name("default","bitWidth"))
    newtext = doc.createTextNode(str(field.width))
    newel.appendChild(newtext)
    father_node.appendChild(newel)

# done : access to ipxact mapping, access and modifieldWriteValue
    if field.access =='RW': # read-write
        field.access = "read-write"
    elif field.access =='WO': # write-only
        field.access = "write-only"
    elif field.access =='RO': # read-only
        field.access = "read-only"
    elif field.access =='W1C': # read-write
        field.access = "read-write"
        field.modified_write_value='oneToClear'
    elif field.access =='RC': # read-only
        field.access = "read-only"
        field.read_action='clear'

    newel = doc.createElement(ns_name("default","access"))
    newtext = doc.createTextNode(field.access)
    newel.appendChild(newtext)
    father_node.appendChild(newel)

    if field.modified_write_value != '': 
        newel = doc.createElement(ns_name("default","modifiedWriteValue"))
        newtext = doc.createTextNode(field.modified_write_value)
        newel.appendChild(newtext)
        father_node.appendChild(newel)

    if field.read_action != '': 
        newel = doc.createElement(ns_name("default","readAction"))
        newtext = doc.createTextNode(field.read_action)
        newel.appendChild(newtext)
        father_node.appendChild(newel)

    newel = doc.createElement(ns_name("default","resets"))
    father_node.appendChild(newel)

    newel_1 = doc.createElement(ns_name("default","reset"))
    newel.appendChild(newel_1)

    newel_2 = doc.createElement(ns_name("default","value"))
    newtext = doc.createTextNode(field.reset_value)
    newel_2.appendChild(newtext)
    newel_1.appendChild(newel_2)

    newel_2 = doc.createElement(ns_name("default","mask"))
    newtext = doc.createTextNode(field.reset_mask)
    newel_2.appendChild(newtext)
    newel_1.appendChild(newel_2)

# fill reg information
def fill_reg_info(reg,father_node):
    newel = doc.createElement(ns_name("default","name"))
    newtext = doc.createTextNode(reg.name)
    newel.appendChild(newtext)
    father_node.appendChild(newel)

    newel = doc.createElement(ns_name("default","displayName"))
    newtext = doc.createTextNode(reg.full_name)
    newel.appendChild(newtext)
    father_node.appendChild(newel)

    newel = doc.createElement(ns_name("default","description"))
    newtext = doc.createTextNode(reg.description)
    newel.appendChild(newtext)
    father_node.appendChild(newel)

    newel = doc.createElement(ns_name("default","addressOffset"))
    newtext = doc.createTextNode(reg.offset)
    newel.appendChild(newtext)
    father_node.appendChild(newel)


    if reg.access =='RW': # read-write
        reg.access = "read-write"
    elif reg.access =='WO': # write-only
        reg.access = "write-only"
    elif reg.access =='RO': # read-only
        reg.access = "read-only"
    newel = doc.createElement(ns_name("default","access"))
    newtext = doc.createTextNode(reg.access)
    newel.appendChild(newtext)
    father_node.appendChild(newel)

    newel = doc.createElement(ns_name("default","size"))
    newtext = doc.createTextNode(str(reg.size))
    newel.appendChild(newtext)
    father_node.appendChild(newel)

    if reg.volatile == 'true': 
        newel = doc.createElement(ns_name("default","volatile"))
        newtext = doc.createTextNode(reg.volatile)
        newel.appendChild(newtext)
        father_node.appendChild(newel)

    newel = doc.createElement(ns_name("default","resets"))
    father_node.appendChild(newel)

    newel_1 = doc.createElement(ns_name("default","reset"))
    newel.appendChild(newel_1)

    newel_2 = doc.createElement(ns_name("default","value"))
    newtext = doc.createTextNode(reg.reset_value)
    newel_2.appendChild(newtext)
    newel_1.appendChild(newel_2)

    newel_2 = doc.createElement(ns_name("default","mask"))
    newtext = doc.createTextNode(reg.reset_mask)
    newel_2.appendChild(newtext)
    newel_1.appendChild(newel_2)

    # for field in reg.fields:
    #     newel = doc.createElement(ns_name("default","field"))
    #     father_node.appendChild(newel)
    #     fill_field_info(reg.fields[field],newel)

# fill block information 
def fill_block_info(block,father_node):
    newel = doc.createElement(ns_name("default","name"))  
    newtext = doc.createTextNode(block.name)
    newel.appendChild(newtext)
    father_node.appendChild(newel)
 
    newel = doc.createElement(ns_name("default","displayName"))  
    newtext = doc.createTextNode(block.full_name)
    newel.appendChild(newtext)
    father_node.appendChild(newel)

    newel = doc.createElement(ns_name("default","baseAddress"))  
    newtext = doc.createTextNode(block.base_address)
    newel.appendChild(newtext)
    father_node.appendChild(newel)

    newel = doc.createElement(ns_name("default","range"))  
    newtext = doc.createTextNode(str(block.range))
    newel.appendChild(newtext)
    father_node.appendChild(newel)

    newel = doc.createElement(ns_name("default","width"))  
    newtext = doc.createTextNode(str(block.data_width))
    newel.appendChild(newtext)
    father_node.appendChild(newel)

    cur_nod = newel
    return cur_nod

    # for reg in block.regs:
    #     newel = doc.createElement(ns_name("default","register"))
    #     father_node.appendChild(newel)
    #     fill_reg_info(block.regs[reg],newel)

def gen_xml(top):
    root = doc.createElement(ns_name("default","component")) 
    for key in NS:
        root.setAttribute("xmlns:{}".format(NS[key]["ns"]), NS[key]["uri"])  
    doc.appendChild(root)  
 
    newel_0 = doc.createElement(ns_name("default","vendor"))  
    newtext = doc.createTextNode("armchina")
    newel_0.appendChild(newtext)
    root.appendChild(newel_0)
 
    newel_0 = doc.createElement(ns_name("default","library"))  
    newtext = doc.createTextNode("zhouyi")
    newel_0.appendChild(newtext)
    root.appendChild(newel_0)

    newel_0 = doc.createElement(ns_name("default","name"))  
    newtext = doc.createTextNode(top.pjname)
    newel_0.appendChild(newtext)
    root.appendChild(newel_0)

    newel_0 = doc.createElement(ns_name("default","version"))  
    newtext = doc.createTextNode("1.0")
    newel_0.appendChild(newtext)
    root.appendChild(newel_0)

    newel_0 = doc.createElement(ns_name("default","memoryMaps"))  
    root.appendChild(newel_0)

    newel_1 = doc.createElement(ns_name("default","memoryMap"))
    newel_0.appendChild(newel_1)

    newel_2 = doc.createElement(ns_name("default","name"))
    mmp_name = top.abbre_name.strip().replace(' ','_')
    newtext = doc.createTextNode(mmp_name)
    newel_2.appendChild(newtext)
    newel_1.appendChild(newel_2)

    newel_2 = doc.createElement(ns_name("default","addressUnitBits"))
    newtext = doc.createTextNode(str(top.addr_unit_bits))
    newel_2.appendChild(newtext)
    newel_1.appendChild(newel_2)

    if merge_block == False:
        for block in top.blocks:
            newel_2 = doc.createElement(ns_name("default","addressBlock"))
            newel_1.appendChild(newel_2)
            fill_block_info(top.blocks[block],newel_2)
            for reg in block.regs:
                newel = doc.createElement(ns_name("default","register"))
                father_node.appendChild(newel)
                fill_reg_info(block.regs[reg],newel)
                for field in reg.fields:
                    newel = doc.createElement(ns_name("default","field"))
                    father_node.appendChild(newel)
                    fill_field_info(reg.fields[field],newel)
    elif merge_block == True:
        for block in top.blocks:
            newel_2 = doc.createElement(ns_name("default","addressBlock"))
            newel_1.appendChild(newel_2)
            fill_block_info(top.blocks[block],newel_2)
            for reg in block.regs:
                newel = doc.createElement(ns_name("default","register"))
                father_node.appendChild(newel)
                fill_reg_info(block.regs[reg],newel)
                for field in reg.fields:
                    newel = doc.createElement(ns_name("default","field"))
                    father_node.appendChild(newel)
                    fill_field_info(reg.fields[field],newel)

    return doc

if __name__ == "__main__":  
    import os
    os.chdir(os.path.dirname(os.path.realpath(__file__)))
    from extract_info import *

    top,inst_top=get_demo_reg_tree()
    xml=gen_xml(inst_top)
    f = open("Register.xml", "wb+")  
    f.write(doc.toprettyxml(indent = "\t", newl = "\n", encoding = "utf-8"))  
    # doc.writexml(f)
    f.close()
