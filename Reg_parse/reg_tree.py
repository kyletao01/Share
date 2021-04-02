import sys
import re
import os
import copy
class base_reg(object):
    template       = dict()
    datawidth      = dict()
    data_width     = 32

    def __init__(self,name):
        self.name           = name
        self.description    = ""
        self.full_name      = "" 
        self.inst           = name
        self.num            = 1
        self.level          = 0

    def print_var(self,level=0,var="",val="") :
        print("%(spc)s%(vr)-10s= %(val)s" % {"spc":"    "*level,"vr":var,"val":val})

class field(base_reg):

    def __init__(self,name):
        super(field,self).__init__(name)
        self.width          = 0
        self.access         = ""
        self.reset_value    = "0x0"
        self.reset_mask     = "0xffff_ffff"
        self.bits           = "" 
        self.msb            = 0
        self.lsb            = 0
        self.lct            = [] 
        self.w1c_bit        = 0 ##TODO
        self.no_reset       = 0 ## 0: has reset_value;  1: no reset_value
        self.rtl_access     = []
        #self.raw            = "" 
        self.bitoffset      = 0
        self.bitwidth       = 0
        self.modified_write_value = ""
        self.read_action    = ""
        self.rtl_io_access  = ""
        self.fld_clr_l      = ""

    def update_bits(self):
        if(':' in self.bits):
            self.msb = int(self.bits.split(":")[0])
            self.lsb = int(self.bits.split(":")[1])
        else:
            self.msb = int(self.bits)
            self.lsb = int(self.bits)

class register(base_reg):

    def __init__(self,name):
        super(register,self).__init__(name)
        self.fields         = dict() 
        self.offset         = ""
        self.size           = 0
        self.access         = ""
        self.reset_value    = "0x0"
        self.reset_mask     = "0xffff_ffff"
        self.type_num       = 0 
        self.index          = []
        self.reg_addr_offset= "0x4"
    
    def add_field(self, fld):
        if(isfield(fld)):
            self.fields[fld.name] = fld 
        else:
            print('Add field failed: input type is not field')

    def gen_reset_value(self):
        self.reset_value = ""
        for key,fld in self.fields.items():
            self.reset_value = self.reset_value | (fld.reset_value<<fld.lsb)

class block(base_reg):
    def __init__(self,name):
        super(block,self).__init__(name)
        self.regs           = dict()
        self.blocks         = dict()
        self.base           = 0
        self.base_address   = "0x0"
        self.range          = 2**32
        self.parameters     = list()
        self.address_width  = 0
        self.wdatawidth     = 32
        #self.regs = []
        self.addr_unit_bits = 0
        self.reg_addr_offset= "0x4"
        self.bus_reg_out    = 0
        self.wdata_bp       = 0
        self.add_unit_bits  = 8
        self.path  = ""
        self.sub_block_info = list()

    def add_block(self,vr_block) :
        if(isblock(vr_block)):
            self.blocks[vr_block.name] = vr_block 
        else:
            print('Add block failed: input type is not block')

    def add_reg(self,vr_reg) :
        if(isreg(vr_reg)):
            self.regs[vr_reg.name] = vr_reg 
        else:
            print('Add reg failed: input type is not reg')




def isfield(fld):
    type_str = str(type(fld)).replace("<class '",'').replace("'>",'')
    if(type_str=='reg_tree.field'):
        return 1
    else:
        return 0

def isblock(vr_block):
    type_str = str(type(vr_block)).replace("<class '",'').replace("'>",'')
    if(type_str=='reg_tree.block'):
        return 1
    else:
        return 0

def isreg(vr_reg):
    type_str = str(type(vr_reg)).replace("<class '",'').replace("'>",'')
    if(type_str=='reg_tree.register'):
        return 1
    else:
        return 0