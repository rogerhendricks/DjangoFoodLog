var ctx = document.getElementById('dailyRatioChart');

// const fatRatioChart = document.getElementById('fatRatio').value
function ratioChart(){
  console.log(tcr.innerText)
  const foodRatioChart = new Chart(ctx,{
    type: 'pie',
    data: {
      labels: [
        'Carbs',
        'Protein',
        'Fat'
      ],
      datasets: [{
        label: 'Macro Ratio',
        data: [tcr, tpr, tfr],
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



