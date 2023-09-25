import { json } from '@sveltejs/kit';

export async function POST(requestEvent) {
    try {
        const { request } = requestEvent;
        const received_data = await request.json();
        
        const response = await fetch('http://193.168.1.30:4000/traditional', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify(received_data),
        });
      
        if (!response.ok) {
          throw new Error('Network response was not ok');
        }
      
        const transit_data = await response.json();
        
        return json({ transit_data });
    } catch (error) {
        console.error('Error fetching data:', error);
        return json({ error: 'Failed to fetch data' }, { status: 500 });
    }
}
