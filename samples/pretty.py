import os
import xml.etree.ElementTree as ETree

def indent(elem, level=0):
  i = "\n" + level*"  "
  if len(elem):
    if not elem.text or not elem.text.strip():
      elem.text = i + "  "
    if not elem.tail or not elem.tail.strip():
      elem.tail = i
    for elem in elem:
      indent(elem, level+1)
    if not elem.tail or not elem.tail.strip():
      elem.tail = i
  else:
    if level and (not elem.tail or not elem.tail.strip()):
      elem.tail = i
      
if len(os.sys.argv) < 2:
    print("Not enough param: A xml file is need.")
    os.system(exit(1))

strategy_xml = os.sys.argv[1]
pretty = True;
if len(os.sys.argv) > 2:
    switch = os.sys.argv[2]
    if switch == "false":
        pretty = False
    
tree = ETree.parse(strategy_xml)
root = tree.getroot()
for strategy_node in root:
    conditions_node = strategy_node.find("conditions")
    condition_node = conditions_node.find("condition")
    old_value = condition_node.get("time")
    new_value = int(old_value)
    new_value += 1
    condition_node.set("time",str(new_value))
    
if pretty:
    indent(root)
tree.write("./out.xml",encoding="UTF-8",xml_declaration=True)