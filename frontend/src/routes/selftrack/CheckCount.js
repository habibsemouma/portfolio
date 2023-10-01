export function get_check_count_options(get_check_count_data) {
  return {
    title: {
      text: "Number of phone checks by day",
    },
    chart: {
      type: "bar",
      height: 300,
    },
    plotOptions: {
      bar: {
        horizontal: true,
        colors: {
          ranges: [
            {
              from: 0,
              to: 90,
              color: "#FF5733",
            },
            {
              from: 90,
              to: 120,
              color: "#2290E2",
            },
            {
              from: 120,
              to: 500,
              color: "#5733FF",
            },
          ],
          backgroundBarColors: ["#F0F0F0"], // Background color for bars not in the specified ranges
        },
      },
    },
    xaxis: {
      categories: get_check_count_data.date,
      title: {
        text: "Number of checks",
      },
    },
    yaxis: {
      title: {
        text: "Days",
      },
    },
    series: [
      {
        name: "Series 1",
        data: get_check_count_data.checkcount,
      },
    ],
  };
}
