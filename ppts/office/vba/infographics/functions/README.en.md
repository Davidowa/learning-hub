# VBA functions and Excel functions in VBA

This English handout contains two Letter pages. The first explains the inputs and return value of a VBA Function, ByVal, the return type, and assignment to the function name. It shows how to call the function from a Sub and from a worksheet cell. The second explains WorksheetFunction, Range arguments, storing a calculated value, storing a formula, and checking a lookup result with IsError.

The design follows the Learning Hub VBA palette in ppts/kit/tokens.py. The images were generated with the built-in ImageGen tool and reviewed for code accuracy and legibility. The final prompts and editable text are in fuentes. The PDF embeds the two images; the PNG files and the text notes are provided separately.

## Use the examples

In desktop Excel, open the Visual Basic Editor. Import FunctionsExamples.bas into the intended workbook project through File > Import File. If you paste the code into a standard module instead, omit the Attribute VB_Name line. Save the workbook as .xlsm, and allow macros for this trusted workbook.

Run Demo to print 108 in the Immediate window. For the worksheet example, enter 100 in A2 and 0.08 in B2 on a separate example sheet. Enter =WithTax(A2,B2) in C2, using the formula separator required by your regional settings.

For Summarize and StoreFormula, create a worksheet named Data in the workbook that contains the module. Enter 10, 20, 30, and 40 in B2:B5. Summarize writes the calculated value 100 to D2. StoreFormula writes a SUM formula to D3, which updates when Excel recalculates. These procedures write only those output cells.

For FindCode, enter product codes in Data!A2:A5. The procedure searches for P-02 and displays its position within that range, or displays Not found. It leaves the worksheet unchanged.

## Review scope

The examples were reviewed against official Microsoft documentation. The PDF page count, Letter page size, image placement, text, and code were inspected. The VBA module has not been compiled or executed in Excel during this task.

## References

- Function statement: https://learn.microsoft.com/en-us/office/vba/language/reference/user-interface-help/function-statement
- Passing arguments by value: https://learn.microsoft.com/en-us/office/vba/language/concepts/getting-started/passing-arguments-efficiently
- Creating custom functions: https://support.microsoft.com/en-us/excel/create-custom-functions-in-excel
- Using worksheet functions in VBA: https://learn.microsoft.com/en-us/office/vba/excel/concepts/events-worksheetfunctions-shapes/using-excel-worksheet-functions-in-visual-basic
- Match: https://learn.microsoft.com/en-us/office/vba/api/excel.worksheetfunction.match
- Range.Formula: https://learn.microsoft.com/en-us/office/vba/api/excel.range.formula
- Range.FormulaLocal: https://learn.microsoft.com/en-us/office/vba/api/excel.range.formulalocal
