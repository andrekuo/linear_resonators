
from qiskit_metal.qlibrary.terminations.launchpad_wb import LaunchpadWirebond

from qiskit_metal.qlibrary.terminations.open_to_ground import OpenToGround

from qiskit_metal.qlibrary.couplers.coupled_line_tee import CoupledLineTee

from qiskit_metal.qlibrary.tlines.straight_path import RouteStraight

from qiskit_metal.qlibrary.tlines.meandered import RouteMeander

from qiskit_metal import designs, MetalGUI

design = designs.DesignPlanar()

gui = MetalGUI(design)


wb_top = LaunchpadWirebond(
design,
name='wb_top',
options={'orientation': -90,
 'pos_y': 2.2,
 'trace_gap': '5.1um',
 'trace_width': '11.7um'},

component_template=None,
)




wb_bottom = LaunchpadWirebond(
design,
name='wb_bottom',
options={'orientation': 90,
 'pos_y': -2.2,
 'trace_gap': '5.1um',
 'trace_width': '11.7um'},

component_template=None,
)




otg1 = OpenToGround(
design,
name='otg1',
options={'orientation': '90',
 'pos_x': '-1250um',
 'pos_y': '1200um'},

component_template=None,
)




clt1 = CoupledLineTee(
design,
name='clt1',
options={'coupling_length': '225um',
 'coupling_space': '7.9um',
 'open_termination': False,
 'orientation': '-90',
 'pos_y': '1200um',
 'prime_gap': '5.1um',
 'prime_width': '11.7um',
 'second_gap': '5.1um',
 'second_width': '11.7um'},

component_template=None,
)




cpw1 = RouteMeander(
design,
name='cpw1',
options={'_actual_length': '3.8150000000000004 '
                   'mm',
 'fillet': '49.9um',
 'lead': {'end_jogged_extension': '',
          'end_straight': '0mm',
          'start_jogged_extension': '',
          'start_straight': '50um'},
 'meander': {'asymmetry': '0um',
             'spacing': '100um'},
 'pin_inputs': {'end_pin': {'component': 'otg1',
                            'pin': 'open'},
                'start_pin': {'component': 'clt1',
                              'pin': 'second_end'}},
 'total_length': '3815um',
 'trace_gap': '5.1um',
 'trace_width': '11.7um'},

type='CPW',
)




otg2 = OpenToGround(
design,
name='otg2',
options={'orientation': '-90',
 'pos_x': '1250um',
 'pos_y': '1700um'},

component_template=None,
)




clt2 = CoupledLineTee(
design,
name='clt2',
options={'coupling_length': '225um',
 'coupling_space': '7.9um',
 'open_termination': False,
 'orientation': '90',
 'pos_y': '1700um',
 'prime_gap': '5.1um',
 'prime_width': '11.7um',
 'second_gap': '5.1um',
 'second_width': '11.7um'},

component_template=None,
)




cpw2 = RouteMeander(
design,
name='cpw2',
options={'_actual_length': '3.714999999999999 '
                   'mm',
 'fillet': '49.9um',
 'lead': {'end_jogged_extension': '',
          'end_straight': '0mm',
          'start_jogged_extension': '',
          'start_straight': '50um'},
 'meander': {'asymmetry': '0um',
             'spacing': '100um'},
 'pin_inputs': {'end_pin': {'component': 'otg2',
                            'pin': 'open'},
                'start_pin': {'component': 'clt2',
                              'pin': 'second_end'}},
 'total_length': '3715um',
 'trace_gap': '5.1um',
 'trace_width': '11.7um'},

type='CPW',
)




otg3 = OpenToGround(
design,
name='otg3',
options={'orientation': '90',
 'pos_x': '-1250um',
 'pos_y': '-300um'},

component_template=None,
)




clt3 = CoupledLineTee(
design,
name='clt3',
options={'coupling_length': '225um',
 'coupling_space': '7.9um',
 'open_termination': False,
 'orientation': '-90',
 'pos_y': '-300um',
 'prime_gap': '5.1um',
 'prime_width': '11.7um',
 'second_gap': '5.1um',
 'second_width': '11.7um'},

component_template=None,
)




cpw3 = RouteMeander(
design,
name='cpw3',
options={'_actual_length': '3.62 mm',
 'fillet': '49.9um',
 'lead': {'end_jogged_extension': '',
          'end_straight': '0mm',
          'start_jogged_extension': '',
          'start_straight': '50um'},
 'meander': {'asymmetry': '0um',
             'spacing': '100um'},
 'pin_inputs': {'end_pin': {'component': 'otg3',
                            'pin': 'open'},
                'start_pin': {'component': 'clt3',
                              'pin': 'second_end'}},
 'total_length': '3620um',
 'trace_gap': '5.1um',
 'trace_width': '11.7um'},

type='CPW',
)




otg4 = OpenToGround(
design,
name='otg4',
options={'orientation': '-90',
 'pos_x': '1250um',
 'pos_y': '250um'},

component_template=None,
)




clt4 = CoupledLineTee(
design,
name='clt4',
options={'coupling_length': '225um',
 'coupling_space': '7.9um',
 'open_termination': False,
 'orientation': '90',
 'pos_y': '250um',
 'prime_gap': '5.1um',
 'prime_width': '11.7um',
 'second_gap': '5.1um',
 'second_width': '11.7um'},

component_template=None,
)




cpw4 = RouteMeander(
design,
name='cpw4',
options={'_actual_length': '3.535 mm',
 'fillet': '49.9um',
 'lead': {'end_jogged_extension': '',
          'end_straight': '0mm',
          'start_jogged_extension': '',
          'start_straight': '50um'},
 'meander': {'asymmetry': '0um',
             'spacing': '100um'},
 'pin_inputs': {'end_pin': {'component': 'otg4',
                            'pin': 'open'},
                'start_pin': {'component': 'clt4',
                              'pin': 'second_end'}},
 'total_length': '3535um',
 'trace_gap': '5.1um',
 'trace_width': '11.7um'},

type='CPW',
)




otg5 = OpenToGround(
design,
name='otg5',
options={'orientation': '90',
 'pos_x': '-1250um',
 'pos_y': '-1500um'},

component_template=None,
)




clt5 = CoupledLineTee(
design,
name='clt5',
options={'coupling_length': '225um',
 'coupling_space': '7.9um',
 'open_termination': False,
 'orientation': '-90',
 'pos_y': '-1500um',
 'prime_gap': '5.1um',
 'prime_width': '11.7um',
 'second_gap': '5.1um',
 'second_width': '11.7um'},

component_template=None,
)




cpw5 = RouteMeander(
design,
name='cpw5',
options={'_actual_length': '3.4499999999999993 '
                   'mm',
 'fillet': '49.9um',
 'lead': {'end_jogged_extension': '',
          'end_straight': '0mm',
          'start_jogged_extension': '',
          'start_straight': '50um'},
 'meander': {'asymmetry': '0um',
             'spacing': '100um'},
 'pin_inputs': {'end_pin': {'component': 'otg5',
                            'pin': 'open'},
                'start_pin': {'component': 'clt5',
                              'pin': 'second_end'}},
 'total_length': '3450um',
 'trace_gap': '5.1um',
 'trace_width': '11.7um'},

type='CPW',
)




otg6 = OpenToGround(
design,
name='otg6',
options={'orientation': '-90',
 'pos_x': '1250um',
 'pos_y': '-1000um'},

component_template=None,
)




clt6 = CoupledLineTee(
design,
name='clt6',
options={'coupling_length': '225um',
 'coupling_space': '7.9um',
 'open_termination': False,
 'orientation': '90',
 'pos_y': '-1000um',
 'prime_gap': '5.1um',
 'prime_width': '11.7um',
 'second_gap': '5.1um',
 'second_width': '11.7um'},

component_template=None,
)




cpw6 = RouteMeander(
design,
name='cpw6',
options={'_actual_length': '3.375000000000001 '
                   'mm',
 'fillet': '49.9um',
 'lead': {'end_jogged_extension': '',
          'end_straight': '0mm',
          'start_jogged_extension': '',
          'start_straight': '50um'},
 'meander': {'asymmetry': '0um',
             'spacing': '100um'},
 'pin_inputs': {'end_pin': {'component': 'otg6',
                            'pin': 'open'},
                'start_pin': {'component': 'clt6',
                              'pin': 'second_end'}},
 'total_length': '3375um',
 'trace_gap': '5.1um',
 'trace_width': '11.7um'},

type='CPW',
)




feedline = RouteStraight(
design,
name='feedline',
options={'_actual_length': '4.35 mm',
 'pin_inputs': {'end_pin': {'component': 'wb_bottom',
                            'pin': 'tie'},
                'start_pin': {'component': 'wb_top',
                              'pin': 'tie'}},
 'trace_gap': '5.1um',
 'trace_width': '11.7um'},

type='CPW',
)



gui.rebuild()
gui.autoscale()
        