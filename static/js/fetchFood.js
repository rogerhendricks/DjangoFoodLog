console.log('fetchFood loaded');
let coke = "5449000000996";
let nutella = "3017620422003"


async function fetchFood(){
  console.log('button pressed');
  let barcode = document.getElementById('foodSearch').value;
  const url = `https://world.openfoodfacts.org/api/v0/product/${barcode}.json`;

  let response = await fetch(url);
  if (response.ok) { // if HTTP-status is 200-299
    // get the response body (the method explained below)
    let json = await response.json();
    console.log(json);
    return json;
  } else {
    alert("HTTP-Error: " + response.status);
  }
};


// function displayFood(json){
//     console.log(json.product.nutriments);
//     //document.getElementById('json').innerHTML = json.product.nutriments.carbohydrates_serving;
//     document.getElementById('brandName').innerHTML = json.product.brands;
//     document.getElementById('calories').innerHTML = json['product']['nutriments']['energy-kcal_serving'];
//     document.getElementById('fatsServing').innerHTML = (json.product.nutriments.fat_serving).toFixed(2);
//     document.getElementById('satFatsServing').innerHTML = json['product']['nutriments']['saturated-fat_serving'];
//     document.getElementById('proServing').innerHTML = (json.product.nutriments.proteins_serving).toFixed(2);
//     document.getElementById('carbsServing').innerHTML = (json.product.nutriments.carbohydrates_serving).toFixed(2);
//     document.getElementById('tableSugars').innerHTML = json.product.nutriments.sugars_serving;
// };


function placeFood(json){
    document.getElementById('brandName').value = json.product.brands;
    document.getElementById('calories').value = json['product']['nutriments']['energy-kcal_serving'];
    document.getElementById('tableFats').value = (json.product.nutriments.fat_serving).toFixed(2);
    document.getElementById('tableSatFats').value = (json['product']['nutriments']['saturated-fat_serving']).toFixed(2);
    document.getElementById('tableProtein').value = (json.product.nutriments.proteins_serving).toFixed(2);
    document.getElementById('tableCarbs').value = (json.product.nutriments.carbohydrates_serving).toFixed(2);
    document.getElementById('tableSugars').value = (json.product.nutriments.sugars_serving).toFixed(2);
    document.getElementById('tableSalt').value = (json.product.nutriments.salt).toFixed(2);
}

// function useFood(){
//   document.getElementById('name').value = document.getElementById('brandName').innerHTML;
//   document.getElementById('tableFats').value = document.getElementById('fatsServing').innerHTML;
//   document.getElementById('tableCarbs').value = document.getElementById('carbsServing').innerHTML;
//   document.getElementById('tableProtein').value = document.getElementById('proServing').innerHTML;
// };