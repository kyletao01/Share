`ifndef __OUTPUT_UVMREG_SV__
`define __OUTPUT_UVMREG_SV__
class reg_rfile0_ureg0 extends uvm_reg;
   rand uvm_reg_field destination;
   rand uvm_reg_field frame_kind;
   rand uvm_reg_field rsvd;
   
   virtual function void build();
      destination = uvm_reg_field::type_id::create("destination", null, get_full_name());
      destination.configure(this, 14, 0, "RW", 1, 'h1678, 1, 1, 0);
      frame_kind = uvm_reg_field::type_id::create("frame_kind", null, get_full_name());
      frame_kind.configure(this, 2, 14, "RW", 1, 'h1, 1, 1, 0);
      rsvd = uvm_reg_field::type_id::create("rsvd", null, get_full_name());
      rsvd.configure(this, 16, 16, "RW", 1, 'h1234, 1, 1, 0);
   endfunction

   function new(string name = "reg_rfile0_ureg0");
      super.new(name, 32, UVM_NO_COVERAGE);
   endfunction

   `uvm_object_utils(reg_rfile0_ureg0)
endclass

class reg_rfile0_ureg1 extends uvm_reg;
   rand uvm_reg_field destination;
   rand uvm_reg_field frame_kind;
   rand uvm_reg_field rsvd;
   
   virtual function void build();
      destination = uvm_reg_field::type_id::create("destination", null, get_full_name());
      destination.configure(this, 14, 0, "RW", 1, 'h1678, 1, 1, 0);
      frame_kind = uvm_reg_field::type_id::create("frame_kind", null, get_full_name());
      frame_kind.configure(this, 2, 14, "RW", 1, 'h1, 1, 1, 0);
      rsvd = uvm_reg_field::type_id::create("rsvd", null, get_full_name());
      rsvd.configure(this, 16, 16, "RW", 1, 'h1234, 1, 1, 0);
   endfunction

   function new(string name = "reg_rfile0_ureg1");
      super.new(name, 32, UVM_NO_COVERAGE);
   endfunction

   `uvm_object_utils(reg_rfile0_ureg1)
endclass

class reg_rfile0_ureg2 extends uvm_reg;
   rand uvm_reg_field destination;
   rand uvm_reg_field frame_kind;
   rand uvm_reg_field rsvd;
   
   virtual function void build();
      destination = uvm_reg_field::type_id::create("destination", null, get_full_name());
      destination.configure(this, 14, 0, "W1C", 1, 'h1678, 1, 1, 0);
      frame_kind = uvm_reg_field::type_id::create("frame_kind", null, get_full_name());
      frame_kind.configure(this, 2, 14, "W1C", 1, 'h1, 1, 1, 0);
      rsvd = uvm_reg_field::type_id::create("rsvd", null, get_full_name());
      rsvd.configure(this, 16, 16, "RO", 1, 'h1234, 1, 0, 0);
   endfunction

   function new(string name = "reg_rfile0_ureg2");
      super.new(name, 32, UVM_NO_COVERAGE);
   endfunction

   `uvm_object_utils(reg_rfile0_ureg2)
endclass

class reg_reg_file_ureg3 extends uvm_reg;
   rand uvm_reg_field destination;
   rand uvm_reg_field frame_kind;
   
   virtual function void build();
      destination = uvm_reg_field::type_id::create("destination", null, get_full_name());
      destination.configure(this, 14, 0, "RW", 1, 'h1678, 1, 1, 0);
      frame_kind = uvm_reg_field::type_id::create("frame_kind", null, get_full_name());
      frame_kind.configure(this, 2, 14, "RW", 1, 'h1, 1, 1, 0);
   endfunction

   function new(string name = "reg_reg_file_ureg3");
      super.new(name, 32, UVM_NO_COVERAGE);
   endfunction

   `uvm_object_utils(reg_reg_file_ureg3)
endclass

class reg_reg_file_level2_ureg4 extends uvm_reg;
   rand uvm_reg_field destination;
   rand uvm_reg_field frame_kind;
   
   virtual function void build();
      destination = uvm_reg_field::type_id::create("destination", null, get_full_name());
      destination.configure(this, 14, 0, "RW", 1, 'h1678, 1, 1, 0);
      frame_kind = uvm_reg_field::type_id::create("frame_kind", null, get_full_name());
      frame_kind.configure(this, 2, 14, "RW", 1, 'h1, 1, 1, 0);
   endfunction

   function new(string name = "reg_reg_file_level2_ureg4");
      super.new(name, 32, UVM_NO_COVERAGE);
   endfunction

   `uvm_object_utils(reg_reg_file_level2_ureg4)
endclass

class block_reg_file_reg_file_level2 extends uvm_reg_block;
   rand reg_reg_file_level2_ureg4 ureg4;

   `uvm_object_utils(block_reg_file_reg_file_level2)
   function new(string name = "block_reg_file_reg_file_level2");
      super.new(name, UVM_NO_COVERAGE);
   endfunction 
   
   virtual function void build();
      default_map = create_map("default_map", `UVM_REG_ADDR_WIDTH'h0, 4, UVM_LITTLE_ENDIAN, 1);
      ureg4 = reg_reg_file_level2_ureg4::type_id::create("ureg4");
      ureg4.configure(this, null, "ureg4");
      ureg4.build();
      default_map.add_reg(ureg4, `UVM_REG_ADDR_WIDTH'h14, "RW", 0);
   endfunction
endclass

class block_rfile0_reg_file extends uvm_reg_block;
   rand reg_reg_file_ureg3 ureg3;
   rand block_reg_file_reg_file_level2 reg_file_level2;

   `uvm_object_utils(block_rfile0_reg_file)
   function new(string name = "block_rfile0_reg_file");
      super.new(name, UVM_NO_COVERAGE);
   endfunction 
   
   virtual function void build();
      default_map = create_map("default_map", `UVM_REG_ADDR_WIDTH'h0, 4, UVM_LITTLE_ENDIAN, 1);
      ureg3 = reg_reg_file_ureg3::type_id::create("ureg3");
      ureg3.configure(this, null, "ureg3");
      ureg3.build();
      default_map.add_reg(ureg3, `UVM_REG_ADDR_WIDTH'h10, "RW", 0);
      reg_file_level2 = block_reg_file_reg_file_level2::type_id::create("reg_file_level2",,get_full_name());
      reg_file_level2.configure(this, "");
      reg_file_level2.build();
      default_map.add_submap(reg_file_level2.default_map, `UVM_REG_ADDR_WIDTH'h14);
   endfunction
endclass

class rfile0 extends uvm_reg_block;
   rand reg_rfile0_ureg0 ureg0;
   rand reg_rfile0_ureg1 ureg1;
   rand reg_rfile0_ureg2 ureg2;
   rand block_rfile0_reg_file reg_file;

   `uvm_object_utils(rfile0)
   function new(string name = "rfile0");
      super.new(name, UVM_NO_COVERAGE);
   endfunction 
   
   virtual function void build();
      default_map = create_map("default_map", `UVM_REG_ADDR_WIDTH'h0, 4, UVM_LITTLE_ENDIAN, 1);
      ureg0 = reg_rfile0_ureg0::type_id::create("ureg0");
      ureg0.configure(this, null, "ureg0");
      ureg0.build();
      default_map.add_reg(ureg0, `UVM_REG_ADDR_WIDTH'h0, "RW", 0);
      ureg1 = reg_rfile0_ureg1::type_id::create("ureg1");
      ureg1.configure(this, null, "ureg1");
      ureg1.build();
      default_map.add_reg(ureg1, `UVM_REG_ADDR_WIDTH'h4, "RW", 0);
      ureg2 = reg_rfile0_ureg2::type_id::create("ureg2");
      ureg2.configure(this, null, "ureg2");
      ureg2.build();
      default_map.add_reg(ureg2, `UVM_REG_ADDR_WIDTH'h8, "RW", 0);
      reg_file = block_rfile0_reg_file::type_id::create("reg_file",,get_full_name());
      reg_file.configure(this, "");
      reg_file.build();
      default_map.add_submap(reg_file.default_map, `UVM_REG_ADDR_WIDTH'h10);
   endfunction
endclass

class mem extends uvm_reg_block;

   `uvm_object_utils(mem)
   function new(string name = "mem");
      super.new(name, UVM_NO_COVERAGE);
   endfunction 
   
   virtual function void build();
      default_map = create_map("default_map", `UVM_REG_ADDR_WIDTH'h0, 8, UVM_LITTLE_ENDIAN, 1);
   endfunction
endclass

`endif