import { json } from "@sveltejs/kit";

export async function POST(requestEvent) {
  try {
    const { request } = requestEvent;
    let stream=request.body
    const reader= stream.getReader()
    const {done,value}= await reader.read()
    console.error(value.toString("utf-8"))

    const response = await fetch("http://127.0.0.1:4000/stenhide", {
      method: "POST",
      headers: {
        "Content-Type": "multipart/form-data",
      },
      body: request.body,
    },);

    const transit_data = await response.blob();

    return json({ transit_data });
  } catch (error) {
    console.error("Error fetching data:", error);
    return json({ error: "Failed to fetch data" }, { status: 500 });
  }
}
