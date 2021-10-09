console.log("foodData loaded");

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
        let tfr = parseFloat(i[1]['food__fat_ratio']);
        let tpr = parseFloat(i[1]['food__protein_ratio']);
        let tcr = parseFloat(i[1]['food__carb_ratio']);
        totalFatRatio  += tfr;
        totalProRatio += tpr;
        totalCarbRatio += tcr;
        
      }
      document.getElementById('tfr').innerHTML = (totalFatRatio / todayData.length).toFixed(1) + ' %';
      document.getElementById('tcr').innerHTML = (totalCarbRatio / todayData.length).toFixed(1) + ' %';
      document.getElementById('tpr').innerHTML = (totalProRatio / todayData.length).toFixed(1) + ' %';
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
      document.getElementById('mfr').innerHTML = (monthlyFatRatio / monthlyData.length).toFixed(1) + ' %';
      document.getElementById('mcr').innerHTML = (monthlyCarbRatio / monthlyData.length).toFixed(1) + ' %';
      document.getElementById('mpr').innerHTML = (monthlyProRatio / monthlyData.length).toFixed(1) + ' %';
    }

    dailyMacros();
    monthlyMacros();

}

