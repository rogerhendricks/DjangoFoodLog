console.log("foodData loaded");


var ctx = document.getElementById('dailyRatioChart');
var cty = document.getElementById('monthlyRatioChart');

// const fatRatioChart = document.getElementById('fatRatio').value




function fooddata() {
    //var startDate = new Date("2021-08-31").toISOString().substring(0, 10);
    //var endDate = new Date("2021-09-05");
    var todayDate = new Date()
    var stringDate = todayDate.toISOString().substring(0, 10);
    var month = todayDate.getMonth()+1;
    
    // get daily macro count comparing current date to a.mealDate
    var todayData = ml_data.filter(a => {
      var date = new Date(a.mealDate).toISOString().substring(0, 10);
      //return (date >= startDate && date <= endDate);
      //console.log(stringDate);
      return (date == stringDate);
      
    });
    
    // get monthly macro count comparing current month to a.mealDate ? month
    var monthlyData = ml_data.filter(a => {
      var date = a.mealDate.slice(5, 7);
      return (date == month);
    });

   
    var dailyMacros = () => {
      let totalFatRatio = 0;
      let totalProRatio = 0;
      let totalCarbRatio = 0;
      for (const i of Object.entries(todayData)) {
        let fr = parseFloat(i[1]['food__fat_ratio']);
        let pr = parseFloat(i[1]['food__protein_ratio']);
        let cr = parseFloat(i[1]['food__carb_ratio']);
        totalFatRatio  += fr;
        totalProRatio += pr;
        totalCarbRatio += cr;
      }

      let ttfr = parseFloat((totalFatRatio / todayData.length).toFixed(1));
      document.getElementById('tfr').innerHTML = `${ttfr} %`;
      let ttcr = parseFloat((totalCarbRatio / todayData.length).toFixed(1));
      document.getElementById('tcr').innerHTML = `${ttcr} %`;
      let ttpr = parseFloat((totalProRatio / todayData.length).toFixed(1));
      document.getElementById('tpr').innerHTML = `${ttpr} %`;
      dailyRatioChart(ttfr, ttcr, ttpr);
    }


    var monthlyMacros = () => {
      let monthlyFatRatio = 0;
      let monthlyProRatio = 0;
      let monthlyCarbRatio = 0;
      for (const i of Object.entries(monthlyData)) {
        let mfr = parseFloat(i[1]['food__fat_ratio']);
        let mpr = parseFloat(i[1]['food__protein_ratio']);
        let mcr = parseFloat(i[1]['food__carb_ratio']);
        monthlyFatRatio  += mfr;
        monthlyProRatio += mpr;
        monthlyCarbRatio += mcr;
      }
      let mmfr =parseFloat((monthlyFatRatio / monthlyData.length).toFixed(1));
      document.getElementById('mfr').innerHTML = `${mmfr}%`;
      let mmcr = parseFloat((monthlyCarbRatio / monthlyData.length).toFixed(1));
      document.getElementById('mcr').innerHTML = `${mmcr}%`;
      let mmpr = parseFloat((monthlyProRatio / monthlyData.length).toFixed(1));
      document.getElementById('mpr').innerHTML =  `${mmpr}%`;
      monthlyRatioChart(mmfr, mmcr, mmpr);

    }

    dailyMacros();
    monthlyMacros();

}



function dailyRatioChart(ttfr, ttcr, ttpr){
  
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
        data: [ttcr, ttpr, ttfr],
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

function monthlyRatioChart(mmcr, mmpr, mmfr){
  console.log(mmcr);
  const monthlyfoodRatioChart = new Chart(cty,{
    type: 'pie',
    data: {
      labels: [
        'Carbs',
        'Protein',
        'Fat'
      ],
      datasets: [{
        label: 'Macro Ratio',
        data: [mmcr, mmpr, mmfr],
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