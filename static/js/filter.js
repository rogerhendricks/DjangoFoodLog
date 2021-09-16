function daily(){
  const date = new Date().toISOString().substring(0, 10);
  let mDate = document.querySelectorAll("#isoDate");
  let i;
  for (i = 0; i < mDate.length; i++) {
    //let i = document.getElementById("isoDate").innerText;
    let x = mDate[i].innerText.trim();
    if (x != date){
      mDate[i].parentNode.style.visibility = "hidden";
    }
  }
};

function monthly(){
  let x = document.querySelectorAll(".card");
  let i;
  for (i = 0; x.length; i++){
    x[i].style.visibility = "visible";
  };
}



// let l=0;
// l= favData.length;
// let i=0;
// let select=document.getElementById("select");
// for(i=0;i<l;i++)
// {
// var opt = document.createElement('option');
// opt.value = favData[i].name;
// opt.innerHTML = favData[i].name;
// select.appendChild(opt);
// }