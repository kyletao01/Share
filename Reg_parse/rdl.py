import sys
from systemrdl import RDLCompiler,RDLCompileError

import warnings
with warnings.catch_warnings():
    warnings.simplefilter("ignore")
    from ralbot.ipxact import IPXACTImporter
    from ralbot.ipxact import IPXACTExporter
    from ralbot.uvmgen import uvmGenExporter
    from ralbot.html import HTMLExporter

rdlc=RDLCompiler()
ipxact=IPXACTImporter(rdlc)
try:
    # ipxact.import_file("c:/Users/kyltao01/Desktop/Depositary/Teamp Project/Reg_parse/Register.xml")
    ipxact.import_file("c:/Users/kyltao01/Desktop/IP-XACT REG/reg_tool/reglist.xml")
    rdlc.compile_file("c:/Users/kyltao01/Desktop/Depositary/Teamp Project/Reg_parse/tmp/my.rdl")
    root=rdlc.elaborate()
except RDLCompileError:
    sys.exit(1)

exporter=IPXACTExporter()
exporter.export(root,"c:/Users/kyltao01/Desktop/Depositary/Teamp Project/Reg_parse/tmp/output.xml")

exporter=uvmGenExporter()
exporter.export(root,"c:/Users/kyltao01/Desktop/Depositary/Teamp Project/Reg_parse/tmp/output.sv")

exporter=HTMLExporter()
exporter.export(root,"c:/Users/kyltao01/Desktop/Depositary/Teamp Project/Reg_parse/tmp/output.html")