export function get_check_count_time_options(check_count_time_data) {
  return {
    title: {
      text: "Screentime by days",
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
              to: 10,
              color: "#2290E2",
            },
            {
              from: 10,
              to: 20,
              color: "#FF5733",
            },
            {
              from: 20,
              to: 500,
              color: "#FF0000",
            },
          ],
          backgroundBarColors: ["#F0F0F0"], // Background color for bars not in the specified ranges
        },
      },
    },
    xaxis: {
      categories: check_count_time_data.date,
      title: {
        text: "Hours",
      },
    },
    yaxis: {
      title: {
        text: "Days",
      },
    },
    series: [
      {
        name: "Screen time",
        data: check_count_time_data.screentime,
      },
    ],
  };
}
