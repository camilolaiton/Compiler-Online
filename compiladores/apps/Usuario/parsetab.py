
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'nonassocLESSTHANGREATERTHANleftPLUSMINUSleftTIMESDIVIDErightUMINUSDIVIDE END_OF_SENTENCE EQUALS FALSE GREATERTHAN LESSTHAN LPAREN MINUS NAME NUMBER PLUS PRINT RPAREN STRING TIMES TRUEstatement : NAME EQUALS expression END_OF_SENTENCEstatement : PRINT LPAREN expression RPAREN END_OF_SENTENCEstatement : expression END_OF_SENTENCEexpression : expression PLUS expression\n                  | expression MINUS expression\n                  | expression TIMES expression\n                  | expression DIVIDE expression\n                  | expression LESSTHAN expression\n                  | expression GREATERTHAN expressionexpression : MINUS expression %prec UMINUSexpression : LPAREN expression RPARENexpression : NUMBER\n    \t\t\t  | TRUE\n    \t\t\t  | FALSE\n    \t\t\t  | STRINGexpression : NAME'
    
_lr_action_items = {'NAME':([0,5,6,11,13,14,15,16,17,18,19,],[2,21,21,21,21,21,21,21,21,21,21,]),'PRINT':([0,],[4,]),'MINUS':([0,2,3,5,6,7,8,9,10,11,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,],[6,-16,14,6,6,-12,-13,-14,-15,6,6,6,6,6,6,6,6,14,-16,-10,14,-4,-5,-6,-7,14,14,14,-11,]),'LPAREN':([0,4,5,6,11,13,14,15,16,17,18,19,],[5,19,5,5,5,5,5,5,5,5,5,5,]),'NUMBER':([0,5,6,11,13,14,15,16,17,18,19,],[7,7,7,7,7,7,7,7,7,7,7,]),'TRUE':([0,5,6,11,13,14,15,16,17,18,19,],[8,8,8,8,8,8,8,8,8,8,8,]),'FALSE':([0,5,6,11,13,14,15,16,17,18,19,],[9,9,9,9,9,9,9,9,9,9,9,]),'STRING':([0,5,6,11,13,14,15,16,17,18,19,],[10,10,10,10,10,10,10,10,10,10,10,]),'$end':([1,12,32,34,],[0,-3,-1,-2,]),'EQUALS':([2,],[11,]),'END_OF_SENTENCE':([2,3,7,8,9,10,21,22,23,24,25,26,27,28,29,31,33,],[-16,12,-12,-13,-14,-15,-16,-10,32,-4,-5,-6,-7,-8,-9,-11,34,]),'PLUS':([2,3,7,8,9,10,20,21,22,23,24,25,26,27,28,29,30,31,],[-16,13,-12,-13,-14,-15,13,-16,-10,13,-4,-5,-6,-7,13,13,13,-11,]),'TIMES':([2,3,7,8,9,10,20,21,22,23,24,25,26,27,28,29,30,31,],[-16,15,-12,-13,-14,-15,15,-16,-10,15,15,15,-6,-7,15,15,15,-11,]),'DIVIDE':([2,3,7,8,9,10,20,21,22,23,24,25,26,27,28,29,30,31,],[-16,16,-12,-13,-14,-15,16,-16,-10,16,16,16,-6,-7,16,16,16,-11,]),'LESSTHAN':([2,3,7,8,9,10,20,21,22,23,24,25,26,27,28,29,30,31,],[-16,17,-12,-13,-14,-15,17,-16,-10,17,-4,-5,-6,-7,None,None,17,-11,]),'GREATERTHAN':([2,3,7,8,9,10,20,21,22,23,24,25,26,27,28,29,30,31,],[-16,18,-12,-13,-14,-15,18,-16,-10,18,-4,-5,-6,-7,None,None,18,-11,]),'RPAREN':([7,8,9,10,20,21,22,24,25,26,27,28,29,30,31,],[-12,-13,-14,-15,31,-16,-10,-4,-5,-6,-7,-8,-9,33,-11,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'statement':([0,],[1,]),'expression':([0,5,6,11,13,14,15,16,17,18,19,],[3,20,22,23,24,25,26,27,28,29,30,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> statement","S'",1,None,None,None),
  ('statement -> NAME EQUALS expression END_OF_SENTENCE','statement',4,'p_statement_assign','parser.py',16),
  ('statement -> PRINT LPAREN expression RPAREN END_OF_SENTENCE','statement',5,'p_statement_print','parser.py',24),
  ('statement -> expression END_OF_SENTENCE','statement',2,'p_statement_expr','parser.py',28),
  ('expression -> expression PLUS expression','expression',3,'p_expression_binop','parser.py',31),
  ('expression -> expression MINUS expression','expression',3,'p_expression_binop','parser.py',32),
  ('expression -> expression TIMES expression','expression',3,'p_expression_binop','parser.py',33),
  ('expression -> expression DIVIDE expression','expression',3,'p_expression_binop','parser.py',34),
  ('expression -> expression LESSTHAN expression','expression',3,'p_expression_binop','parser.py',35),
  ('expression -> expression GREATERTHAN expression','expression',3,'p_expression_binop','parser.py',36),
  ('expression -> MINUS expression','expression',2,'p_expression_uminus','parser.py',45),
  ('expression -> LPAREN expression RPAREN','expression',3,'p_expression_group','parser.py',49),
  ('expression -> NUMBER','expression',1,'p_expression_number','parser.py',53),
  ('expression -> TRUE','expression',1,'p_expression_number','parser.py',54),
  ('expression -> FALSE','expression',1,'p_expression_number','parser.py',55),
  ('expression -> STRING','expression',1,'p_expression_number','parser.py',56),
  ('expression -> NAME','expression',1,'p_expression_name','parser.py',60),
]
