import { json } from '@sveltejs/kit';
import axios from "axios";

export async function GET() {
    try {
        const response = await axios.get("http://127.0.0.1:7000/exporter");
        const transit_data = response.data;
        
        return json({ transit_data });
    } catch (error) {
        console.error('Error fetching data:', error);
        return json({ error: 'Failed to fetch data' }, { status: 500 });
    }
}
