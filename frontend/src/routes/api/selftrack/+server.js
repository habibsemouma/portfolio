import { json } from "@sveltejs/kit";

export async function GET() {
  try {
    const response = await fetch("http://193.168.1.40:7000/exporter");

    if (!response.ok) {
      throw new Error("Network response was not ok");
    }

    const transit_data = await response.json();

    return json({ transit_data });
  } catch (error) {
    console.error("Error fetching data:", error);
    return json({ error: "Failed to fetch data" }, { status: 500 });
  }
}
