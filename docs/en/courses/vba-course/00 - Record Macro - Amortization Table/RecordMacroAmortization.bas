Sub GoalSeekAmortization()
    Range("Total_Payment__Monthly").GoalSeek Goal:=0, ChangingCell:=Range("Principal_Amount")
End Sub