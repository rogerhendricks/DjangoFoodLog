console.log('fetchFood loaded');
let coke = "5449000000996";
let nutella = "3017620422003"


async function fetchFood(){
  console.log('button pressed');
  let barcode = document.getElementById('foodSearch').value;
  const url = `https://world.openfoodfacts.org/api/v0/product/${barcode}.json`;
  console.log(url);
  let response = await fetch(url);
  if (response.ok) { // if HTTP-status is 200-299
    // get the response body (the method explained below)
    let json = await response.json();
    console.log(json);
    return json;
    //document.getElementById('name').innerHTML = json.product.brands;
    //document.getElementById('carbs').value = json.product.nutriments.carbohydrates;
    //document.getElementById('pro').value = json.product.nutriments.proteins;
    //document.getElementById('fats').value = json.product.nutriments.fat;
  } else {
    alert("HTTP-Error: " + response.status);
  }
};


function displayFood(json){
    console.log(json.product.nutriments);
    //document.getElementById('json').innerHTML = json.product.nutriments.carbohydrates_serving;
    document.getElementById('brandName').innerHTML = json.product.brands;
    document.getElementById('calServing').innerHTML = json['product']['nutriments']['energy-kcal_serving'];
    document.getElementById('fatsServing').innerHTML = (json.product.nutriments.fat_serving).toFixed(2);
    document.getElementById('satFatsServing').innerHTML = json['product']['nutriments']['saturated-fat_serving'];
    document.getElementById('proServing').innerHTML = (json.product.nutriments.proteins_serving).toFixed(2);
    document.getElementById('carbsServing').innerHTML = (json.product.nutriments.carbohydrates_serving).toFixed(2);
    document.getElementById('sugarsServing').innerHTML = json.product.nutriments.sugars_serving;
};


function useFood(){
  document.getElementById('name').value = document.getElementById('brandName').innerHTML;
  document.getElementById('fats').value = document.getElementById('fatsServing').innerHTML;
  document.getElementById('carbs').value = document.getElementById('carbsServing').innerHTML;
  document.getElementById('protein').value = document.getElementById('proServing').innerHTML;
};