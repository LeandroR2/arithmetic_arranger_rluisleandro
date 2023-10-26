def arithmetic_arranger(problems, show_answers = False):
  #Check if the problem limit has been exceeded
  if len(problems) > 5:
    return "Error: Too many problems."

  arranged_problems = ""
  first_line = ""
  second_line = ""
  dashes_line = ""
  answers_line = ""

  for problem in problems:
  #Divide the problem into operands and operator
    operand1, operator, operand2 = problem.split()

  #Check if the operator is valid
    if operator not in ['+', '-']:
      return "Error: Operator must be '+' or '-'."

  #Check if operands contain only digits
    if not operand1.isdigit() or not operand2.isdigit():
      return "Error: Numbers must only contain digits."

  #Check if operands have more than four digits
    if len(operand1) > 4 or len(operand2) > 4:
      return "Error: Numbers cannot be more than four digits."

  #Determine the number of spaces needed to align the operands
    def max_width():
      if  len(operand1) > len(operand2):
        return len(operand1)
      else:
        return len(operand2)

      #Build the lines for each problem.
    first_line += " "*2 + operand1.rjust(max_width())
    second_line += operator+ " " + operand2.rjust(max_width())
    dashes_line += "-" * (2 + max_width())
    answers_line += " "*(2 + max_width() - len(str(eval(problem))) ) + str(eval(problem)).rjust(max_width())

  #Add spaces between problems
    if problem != problems[-1]:
      first_line +=  " " *4   
      second_line += " " *4
      dashes_line +=  " " *4
      answers_line +=  " " *4

  #Check if the response line should be shown
  if show_answers:
              arranged_problems = "\n".join([first_line, second_line, dashes_line, answers_line])
  else:
              arranged_problems = "\n".join([first_line, second_line, dashes_line])


  return arranged_problems