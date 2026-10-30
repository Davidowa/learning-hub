# Excel functions inside a Sub

This standalone English infographic shows a complete BuildSummary macro that calls Excel's SUM, AVERAGE, and MAX calculations through Application.WorksheetFunction. It writes the calculated numbers to E2:E4 and stores a SUM formula in E6. The example uses a worksheet named Data in the workbook that contains the code.

The lower diagram compares the initial results with the results after B5 changes from 40 to 80. Before the macro runs again, the stored numbers remain 100, 25, and 40. E6 becomes 140 when Excel recalculates. After the macro runs again, the stored numbers become 140, 35, and 80.

## Use the code

Open a sample workbook in desktop Excel, create a worksheet named Data, and enter 10, 20, 30, and 40 in B2:B5. The output cells E2:E4 and E6 should be available for the macro to overwrite. Save the workbook as .xlsm.

Import ExcelFunctionsInSub.bas into that workbook's VBA project through File > Import File in the Visual Basic Editor. To paste the code into a standard module instead, omit the Attribute VB_Name line. Allow macros for this trusted file, then select Developer > Macros > BuildSummary > Run.

## Files and review

The PDF contains one Letter page, 612 by 792 points. The PNG preserves the selected ImageGen output. The editable text is in fuentes. The design uses the Learning Hub VBA palette from ppts/kit/tokens.py.

The code was reviewed against Microsoft documentation, and the numeric examples were checked. The VBA module was not compiled or executed in Excel during this task. The PDF was rendered and inspected for code accuracy, cell references, values, and legibility.

## References

- WorksheetFunction object: https://learn.microsoft.com/en-us/office/vba/api/excel.worksheetfunction
- Sum: https://learn.microsoft.com/en-us/office/vba/api/excel.worksheetfunction.sum
- Average: https://learn.microsoft.com/en-us/office/vba/api/excel.worksheetfunction.average
- Max: https://learn.microsoft.com/en-us/office/vba/api/excel.worksheetfunction.max
- Using worksheet functions in VBA: https://learn.microsoft.com/en-us/office/vba/excel/concepts/events-worksheetfunctions-shapes/using-excel-worksheet-functions-in-visual-basic
- Range.Formula: https://learn.microsoft.com/en-us/office/vba/api/excel.range.formula
