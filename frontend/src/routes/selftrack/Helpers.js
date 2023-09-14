export function get_activity_options(activity_data){
    let series_data=[]

    const keys = Object.keys(activity_data);

    keys.forEach((key) => {
      const value = activity_data[key];
      series_data.push({
        data:value['duration']
      })
    });
    return {
        series: series_data,
        chart: {
        height: 350,
        width:920,
        type: 'area'
      },
      dataLabels: {
        enabled: false
      },
      stroke: {
        curve: 'smooth'
      },
      xaxis: {
        categories: keys
      },
      };
}