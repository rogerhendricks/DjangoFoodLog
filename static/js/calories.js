function combinedCalories(){
  const servingSize = 1; //parseInt(document.getElementById('serving_size').value);
  const fat = parseFloat(document.getElementById('tableFats').value) * servingSize;
  //const fatCals = fat * 9;
  const carbs = parseFloat(document.getElementById('tableCarbs').value);
  //const carbCals = carbs * 4;
  const protein = parseFloat(document.getElementById('tableProtein').value);
  //const protienCals = protein * 4;
  const gramsTotal = fat + carbs + protein;

  const caloriesTotal = (fat * 9) + (carbs * 4) + (protein * 4);
  document.getElementById("calories").value = (caloriesTotal).toFixed(1);
  document.getElementById('fatRatio').value = ((fat / gramsTotal)*100).toFixed(1);
  document.getElementById('carbRatio').value = ((carbs / gramsTotal)*100).toFixed(1);
  document.getElementById('proteinRatio').value = ((protein / gramsTotal)*100).toFixed(1);



const fatRatioChart = document.getElementById('fatRatio').value;
const carbRatioChart = document.getElementById('carbRatio').value;
const proRatioChart = document.getElementById('proteinRatio').value;

createChart(fatRatioChart, carbRatioChart, proRatioChart);


}


function createChart(fatRatioChart, carbRatioChart, proRatioChart){
  var ctx = document.getElementById('ratioChart');

  let chartStatus = Chart.getChart("ratioChart"); // <canvas> id
  if (chartStatus != undefined) {
    chartStatus.destroy();
  }


  const ratioChart = new Chart(ctx,{
    type: 'pie',
    data: {
      labels: [
        'Fat',
        'Carbohydrates',
        'Protein'
      ],
      datasets: [{
        label: 'Macro Ratio',
        data: [fatRatioChart, carbRatioChart, proRatioChart],
        backgroundColor: [
          'rgb(255, 99, 132)',
          'rgb(54, 162, 235)',
          'rgb(255, 205, 86)'
        ],
        hoverOffset: 4
      }]
    },
    options:{
      
    }
  });

}

