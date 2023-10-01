import { json } from "@sveltejs/kit";

export async function POST(requestEvent) {
  try {
    const { request } = requestEvent;

    const response = await fetch("http://127.0.0.1:4000/stenhide", {
      method: "POST",
      headers:{"Content-Type": "multipart/form-data"},
      body: request.body,
    });

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
