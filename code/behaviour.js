function HideDetails(section,img)
{
  document.getElementById(section).style.display="none";
  document.getElementById(img).src="styles/zoom-in-icon.png";
  document.getElementById(img).onclick = function () { ShowDetails(section,img); };
}
function ShowDetails(section,img)
{
  document.getElementById(section).style.display="block";
  document.getElementById(img).src="styles/zoom-out-icon.png";
  document.getElementById(img).onclick = function () { HideDetails(section,img); };	 	
}	
function AddConfig(x)
{
	alert(1);
}
function EditConfig(id,query)
{
	LoadCnfDataRow(id,query);
	document.getElementById("cnfDialog").style.display="block";
}