import { json } from '@sveltejs/kit';
import axios from "axios";

export async function POST({ request, cookies }) {
    try {
        const response = await axios.post("http://127.0.0.1:4000/traditional",request.json);
        const transit_data = response.data;
        
        return json({ transit_data });
    } catch (error) {
        console.error('Error fetching data:', error);
        return json({ error: 'Failed to fetch data' }, { status: 500 });
    }
}
