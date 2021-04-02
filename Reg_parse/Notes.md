# Task
- [ ] register  同名检查
- [ ] filed 同名检查， reserved 后缀重命名。
- [ ] field 检查32bit是否满足
- [ ] check int 0x
- [ ] check index 冲突
- [ ] description 每一个换行换一个paragraph
- [ ] doc/xml 重新将子block收集到top block，去除子block，并重载其地址，path

# Revesion
- 增加了 physical_path
- parameter to parameters
- abbre_name to full_name in reg tree
- physical_path to path
- bit to  bits



    ```
    top_block()
    block  ins_block0(parameter N=1)
    block  ins_block1(parameter N=2)
    ------------------------------------
    block()
    reg reg0(parameter N=1)
    reg reg1(parameter N=1)
    ```



# Discussion
### 1. ipxact reset info of register
- 09  register 有reset
- 14: register 没有reset

### 2. rtl 寄存器索引的 index 和 offset

### 3.  excel 内不能输入指标符Tab

### 4. 参数化的情况：

**Table: reg block**

| reg_block	| address_width	| data_width | base_address	| [parameters] | ... |
| ---- | ---- | ---- | ---- | ---- | ---- |
| tec | 10 | 32 | 0 | N | ... |

**Table: block hierachy**

| BlockInst | BlockName | parameters | AddrOffset | Path |
| ---- | ---- | ---- | ---- | ---- |
| tec | tec0 | N=0 | 0x000 | |
| tec | tec1 | N=1 | 0x020 | |
| tec | tec2 | N=2 | 0x040 | |
| tec | tec3 | N=3 | 0x060 | |


#### 4.1 rtl

```verilog
zy_qian_tec i_tpc_tec [`TPC_TEC_NUM-1:0] (
    ... ...

    .tec_id(tec_id),
    .tec_en(csr_tcer[`TPC_TEC_NUM-1:0]),
    ... ...


module zy_qian_tec_csr (

    // constant
    input  [4:0]                  tec_id,
    ... ...
    ... ...
    wire [`TPC_CSR_WIDTH-1:0] csr_a0 = {4'hf,       // 31:28
                                        3'b0,       // 27:25
                                        tec_id,     // 24:20
                                        1'b0,       // 19
                                        19'b0       // 18:0
                                        };

```

```verilog
module zy_qian_tec_csr #(parameter N=5'b00000) (
    ... ...
    ... ...
```
    
#### 4.1 reg model


```
top_block()
tec_csr_block  tec0(parameter N=0)
tec_csr_block  tec1(parameter N=1)
tec_csr_block  tec1(parameter N=2)
tec_csr_block  tec1(parameter N=3)
```








- 寄存器/block 数组
    

    ```
    block block[N]
    ------------------------------------
    reg reg[N]
    ```

- doc生成标题名样式，
    - 表格中寄存器命名不用增加"Register"结尾，生成doc时会自动添加
    - 缩写名 
    > **B2.1**	ISA Version Register  
    > **B4.1**	AIFF_CTRL (AIFF Configuration Control Register)   
