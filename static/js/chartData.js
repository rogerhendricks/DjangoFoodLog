var ctx = document.getElementById('ratioChart');

const fatRatioChart = document.getElementById('fatRatio').value
const ratioChart = new Chart(ctx,{
  type: 'pie',
  data: {
    labels: [
      'Carbs',
      'Protein',
      'Fat'
    ],
    datasets: [{
      label: 'Macro Ratio',
      data: [fatRatioChart, 50, 100],
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


