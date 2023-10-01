export function get_activity_app_options(activity_app_data) {
  return {
    title: {
      text: "Hours spent on apps",
    },
    chart: {
      type: "bar",
      height: 300,
    },
    plotOptions: {
      bar: {
        horizontal: false,
        colors: {
          ranges: [
            {
              from: 2,
              to: 5,
              color: "#FF5733",
            },
            {
              from: 5,
              to: 11,
              color: "#2290E2",
            },
            {
              from: 11,
              to: 500,
              color: "#5733FF",
            },
          ],
          backgroundBarColors: ["#F0F0F0"], // Background color for bars not in the specified ranges
        },
      },
    },
    xaxis: {
      categories: activity_app_data.name,
      labels: {
        show: false,
      },
      title: {
        text: "Apps",
      },
    },
    yaxis: {
      title: {
        text: "Hours",
      },
    },
    series: [
      {
        name: "Series 1",
        data: activity_app_data.duration,
      },
    ],
  };
}
