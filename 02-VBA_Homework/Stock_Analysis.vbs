'### Easy
'
'* Create a script that will loop through each year of stock data and grab
'  the total amount of volume each stock had over the year.
'
'* You will also need to display the ticker symbol to coincide with the total volume.
'
'* Your result should look as follows (note: all solution images are for 2015 data).


Sub StockSum()

  ' create variable for holding stock ticker symbol - Letters
  Dim StockSymbol As String

  ' create a counter variable for holding total stock volume - Long Integer
  Dim Ticker_Volume As Long
  TickerVolume = 0

  ' variable for holding stock volume data in rows starting after header row 1 - Long Integer
  Dim Total_Stock_Volume As Integer
  StockSummaryRow = 2

  ' Loop through some of the stock data
  For i = 2 To 11000

    ' Check if the stock symbol is the same
    If Cells(i + 1, 1).Value <> Cells(i, 1).Value Then

      ' Set the Stock Symbol Name
      StockSymbol = Cells(i, 1).Value

      ' Add to the Stock Symbol count (Rows, Columns) (add to variable rows, column 10)
      TickerVolume = TickerVolume + Cells(i, 7).Value

      ' Print the Stock symbol in the summary column I
      Range("I" & StockSummaryRow).Value = StockSymbol

      ' Print the total stock volume to the total stock volume columns
      Range("J" & StockSummaryRow).Value = TickerVolume

      ' Add one row to the StockSummaryRow
      StockSummaryRow = StockSummaryRow + 1
      
      ' Reset the Brand Total
      TickerVolume = 0

    ' If the cell immediately following a row is the same brand...
    Else

      ' Add to the Ticker Volume Total
      TickerVolume = TickerVolume + Cells(i, 7).Value

    End If

  Next i

End Sub

