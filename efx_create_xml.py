xml_template = '''
<efx:project name="temp" description="" last_change="1728622663" sw_version="2024.1.163" last_run_state="" last_run_flow="" config_result_in_sync="true" design_ood="" place_ood="" route_ood="" xmlns:efx="http://www.efinixinc.com/enf_proj" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://www.efinixinc.com/enf_proj enf_proj.xsd">
    <efx:device_info>
        <efx:family name="Trion"/>
        <efx:device name="T120F324"/>
        <efx:timing_model name="C4"/>
    </efx:device_info>
    <efx:design_info def_veri_version="verilog_2k" def_vhdl_version="vhdl_2008">
        <efx:top_module name="top"/>
        <efx:top_vhdl_arch name=""/>
    </efx:design_info>
    <efx:constraint_info>
        <efx:inter_file name=""/>
    </efx:constraint_info>
    <efx:sim_info/>
    <efx:misc_info/>
    <efx:ip_info/>
    <efx:synthesis tool_name="efx_map">
        <efx:param name="work_dir" value="work_syn" value_type="e_string"/>
        <efx:param name="write_efx_verilog" value="on" value_type="e_bool"/>
        <efx:param name="allow-const-ram-index" value="0" value_type="e_option"/>
        <efx:param name="blackbox-error" value="1" value_type="e_option"/>
        <efx:param name="blast_const_operand_adders" value="1" value_type="e_option"/>
        <efx:param name="bram_output_regs_packing" value="1" value_type="e_option"/>
        <efx:param name="bram-push-tco-outreg" value="0" value_type="e_option"/>
        <efx:param name="create-onehot-fsms" value="0" value_type="e_option"/>
        <efx:param name="fanout-limit" value="0" value_type="e_integer"/>
        <efx:param name="hdl-compile-unit" value="1" value_type="e_option"/>
        <efx:param name="infer-clk-enable" value="3" value_type="e_option"/>
        <efx:param name="infer-sync-set-reset" value="1" value_type="e_option"/>
        <efx:param name="max_ram" value="-1" value_type="e_integer"/>
        <efx:param name="max_mult" value="-1" value_type="e_integer"/>
        <efx:param name="min-sr-fanout" value="0" value_type="e_integer"/>
        <efx:param name="min-ce-fanout" value="0" value_type="e_integer"/>
        <efx:param name="mode" value="speed" value_type="e_option"/>
        <efx:param name="mult-auto-pipeline" value="0" value_type="e_integer"/>
        <efx:param name="mult-decomp-retime" value="0" value_type="e_option"/>
        <efx:param name="operator-sharing" value="0" value_type="e_option"/>
        <efx:param name="optimize-adder-tree" value="0" value_type="e_option"/>
        <efx:param name="optimize-zero-init-rom" value="1" value_type="e_option"/>
        <efx:param name="retiming" value="1" value_type="e_option"/>
        <efx:param name="seq_opt" value="1" value_type="e_option"/>
        <efx:param name="seq-opt-sync-only" value="0" value_type="e_option"/>
        <efx:param name="use-logic-for-small-mem" value="64" value_type="e_integer"/>
        <efx:param name="use-logic-for-small-rom" value="64" value_type="e_integer"/>
        <efx:param name="mult_input_regs_packing" value="1" value_type="e_option"/>
        <efx:param name="mult_output_regs_packing" value="1" value_type="e_option"/>
    </efx:synthesis>
    <efx:place_and_route tool_name="efx_pnr">
        <efx:param name="work_dir" value="work_pnr" value_type="e_string"/>
        <efx:param name="verbose" value="off" value_type="e_bool"/>
        <efx:param name="load_delaym" value="on" value_type="e_bool"/>
        <efx:param name="optimization_level" value="NULL" value_type="e_option"/>
        <efx:param name="seed" value="1" value_type="e_integer"/>
        <efx:param name="placer_effort_level" value="2" value_type="e_option"/>
        <efx:param name="max_threads" value="-1" value_type="e_integer"/>
        <efx:param name="print_critical_path" value="10" value_type="e_integer"/>
    </efx:place_and_route>
    <efx:bitstream_generation tool_name="efx_pgm">
        <efx:param name="mode" value="active" value_type="e_option"/>
        <efx:param name="width" value="1" value_type="e_option"/>
        <efx:param name="enable_roms" value="smart" value_type="e_option"/>
        <efx:param name="spi_low_power_mode" value="on" value_type="e_bool"/>
        <efx:param name="io_weak_pullup" value="on" value_type="e_bool"/>
        <efx:param name="oscillator_clock_divider" value="DIV8" value_type="e_option"/>
        <efx:param name="bitstream_compression" value="off" value_type="e_bool"/>
        <efx:param name="enable_external_master_clock" value="off" value_type="e_bool"/>
        <efx:param name="active_capture_clk_edge" value="posedge" value_type="e_option"/>
        <efx:param name="jtag_usercode" value="0xFFFFFFFF" value_type="e_string"/>
        <efx:param name="release_tri_then_reset" value="on" value_type="e_bool"/>
        <efx:param name="four_byte_addressing" value="off" value_type="e_bool"/>
        <efx:param name="generate_bit" value="on" value_type="e_bool"/>
        <efx:param name="generate_bitbin" value="off" value_type="e_bool"/>
        <efx:param name="generate_hex" value="on" value_type="e_bool"/>
        <efx:param name="generate_hexbin" value="off" value_type="e_bool"/>
        <efx:param name="cold_boot" value="off" value_type="e_bool"/>
        <efx:param name="cascade" value="off" value_type="e_option"/>
    </efx:bitstream_generation>
    <efx:debugger>
        <efx:param name="work_dir" value="work_dbg" value_type="e_string"/>
        <efx:param name="auto_instantiation" value="off" value_type="e_bool"/>
        <efx:param name="profile" value="NONE" value_type="e_string"/>
    </efx:debugger>
</efx:project>'''



from xml.etree import ElementTree as ET
import argparse

search_prelude = '{http://www.efinixinc.com/enf_proj}'

def find(name, tree):
    query = tree.find(f'{search_prelude}{name}')
    if query is not None:
        return query
    else:
        raise Exception(f'didnt find {name} in tree')

def change_top_module(new_top_module, tree):
    design_info = find('design_info', tree)
    top_module = find('top_module', design_info)
    top_module.set('name', new_top_module)

def add_files(verilog_files, tree):
    design_info = find('design_info', tree)
    for file in verilog_files:
        sub = ET.Element(f'{search_prelude}design_file')
        sub.set('name', file) 
        design_info.insert(1, sub)
       
parser = argparse.ArgumentParser()
# TODO: add o option, ie project name and output file name
parser.add_argument('-top_module', help='set top module of the porject')
args, unknowns = parser.parse_known_args()

et = ET.fromstring(xml_template)
tree = ET.ElementTree(et)

if args.top_module:
    change_top_module(args.top_module, tree)

add_files(unknowns, tree)

ET.indent(tree)
with open('project.xml', '+wb') as f:   
    tree.write(f) 
