VERSION 1.0 CLASS
BEGIN
  MultiUse = -1  'True
END
Attribute VB_Name = "Sheet1"
Attribute VB_GlobalNameSpace = False
Attribute VB_Creatable = False
Attribute VB_PredeclaredId = True
Attribute VB_Exposed = True
Sub optimal_route_finder()

Dim city(5) As String


min_time = 10000 '문자라는 형식의 city 배열 선언
For k = 1 To 1000
    Range("P3") = k
    now_time = Range("N9")
    If (now_time < min_time) Then '새로운 min_time이 출현하면
        min_time = now_time '왕을 바꿔라
        
        For j = 1 To 5
            city(j) = Range("j8").Offset(0, j - 1) '최적경로 기록
        Next j
        Range("Q3") = min_time
    End If
Next k

For j = 1 To 5
    Range("r3").Offset(0, j - 1) = city(j)
Next j
    
End Sub
