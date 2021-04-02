from lxml import etree

def validate(xml_path: str, xsd_path: str) -> bool:

    xmlschema_doc = etree.parse(xsd_path)
    xmlschema = etree.XMLSchema(xmlschema_doc)

    xml_doc = etree.parse(xml_path)
    #result = xmlschema.validate(xml_doc)
    #result = xmlschema.assertValid(xml_doc)
    result = xmlschema.assert_(xml_doc)

    return result

result=validate('Register.xml','c:/Users/kyltao01/Desktop/Depositary/Teamp Project/schema/index.xsd')
print(result)
