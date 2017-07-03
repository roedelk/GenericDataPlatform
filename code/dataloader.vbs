Sub LoadCnfDataTable(sectionTable,query)
	'Create Connection
	Set conn = CreateObject("ADODB.Connection")
	conn.Open =  "DSN=PostgreSQL35W;UID=postgres;PWD=pwd;Database=metadb;"
	'Query the Database
	Set rs = CreateObject("ADODB.recordset")
	rs.Open query, conn
	
	tableHTML = "<table class='cnfTable'>" & _
	            "<thead><tr><th/>"
	For Each field In rs.Fields
		tableHTML = tableHTML & "<th class='cnfTableHeader'>"& Ucase(field.Name) &"</th>"
	Next  
	tableHTML = tableHTML & "</tr></thead><tbody>"

	Do Until rs.EOF
		tableHTML = tableHTML & "<tr>"		            
		For Each field In rs.Fields
			If field.Name = "id" Then 
				tableHTML = tableHTML & "<td><img src='styles/folder-icon.png' class='edit-icon' " & _
							"onClick='javascript:EditConfig("& field.Value &","""& query &""")'></td>"				
			End If
			tableHTML = tableHTML & "<td class='cnfTableCell'>"& field.Value &"</td>"
		Next
		rs.moveNext
		tableHTML = tableHTML & "</tr>"
	Loop
	tableHTML = tableHTML & "</tbody></table>"
	 
	rs.close
	conn.Close	 
	document.getElementById(sectionTable).InnerHTML = tableHTML

End Sub

Sub LoadCnfDataRow(id,query)

    'Create Connection
	Set conn = CreateObject("ADODB.Connection")
	conn.Open =  "DSN=PostgreSQL35W;UID=postgres;PWD=pwd;Database=metadb;"
	'Query the Database
	Set rs = CreateObject("ADODB.recordset")
	stmt = query &" WHERE id = " & id
	rs.Open stmt, conn
	
	dialogHTML = "<table><thead><tr><th>Configuration Attribute</th><th>Value</th></tr></thead><tbody>"			        
	
	For Each field In rs.Fields
	
		dialogHTML = dialogHTML & "<tr><td>"& field.Name &"</td><td>"
		If field.Name = "id" Then 
		dialogHTML = dialogHTML & field.Value
		'		tableHTML = tableHTML & "<td><img src='styles/folder-icon.png' class='edit-icon' " & _
		'					"onClick='javascript:EditConfig("& field.Value &","""& query &""")'></td>"				
		Else
			dialogHTML = dialogHTML & "<input type='text' value='"& field.Value &"'>"
		End If			 
		dialogHTML = dialogHTML & "</td></tr>"
	
	Next
	dialogHTML = dialogHTML & "</tbody></table>"
	
	rs.close
	conn.Close	
	document.getElementById("cnfDialog").InnerHTML = dialogHTML
	
End Sub

			