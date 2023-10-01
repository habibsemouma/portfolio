export function get_activity_options(activity_data) {
  const series_data = [];
  const hours = [
    0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
    21, 22, 23,
  ];
  const keys = Object.keys(activity_data);

  keys.forEach((key) => {
    const value = activity_data[key];
    series_data.push({
      data: value.duration,
      name: key,
    });
  });
  return {
    series: series_data,
    title: {
      text: "Minutes spent every hour",
    },
    chart: {
      type: "area",
      height: 250,
    },
    dataLabels: {
      enabled: false,
    },
    stroke: {
      curve: "smooth",
    },
    xaxis: {
      categories: hours,
      title: {
        text: "Hours of the day",
      },
    },
    yaxis: {
      max: 85,
      title: {
        text: "Minutes spent",
      },
    },
  };
}
