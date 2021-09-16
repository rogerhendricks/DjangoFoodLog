function combinedCalories(){
  const servingSize = parseInt(document.getElementById('serving').value);
  const fat = parseFloat(document.getElementById('fats').value) * servingSize;
  //const fatCals = fat * 9;
  const carbs = parseFloat(document.getElementById('carbs').value);
  //const carbCals = carbs * 4;
  const protein = parseFloat(document.getElementById('protein').value);
  //const protienCals = protein * 4;
  const gramsTotal = fat + carbs + protein;

  const caloriesTotal = (fat * 9) + (carbs * 4) + (protein * 4);
  document.getElementById("calories").value = (caloriesTotal).toFixed(1);
  document.getElementById('fatRatio').value = ((fat / gramsTotal)*100).toFixed(1);
  document.getElementById('carbRatio').value = ((carbs / gramsTotal)*100).toFixed(1);
  document.getElementById('proteinRatio').value = ((protein / gramsTotal)*100).toFixed(1);
}