#!/usr/bin/env node

const fetch = require('node-fetch');

async function api_calls () {
    const url = 'http://127.0.0.1:8000/api/v1/tasks/create/';
    const token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzIxMDU3MjUyLCJpYXQiOjE3MjEwNTM2NTIsImp0aSI6IjZlM2U3NzUwMGE4MTQyZjlhZDYyOWZkMmU2YzBkMmY1IiwidXNlcl9pZCI6MX0.YRrqojNgKojOREyUj_5Sq70eTaokkFlzNEXdOKUat-w';

    try {
         const response = await fetch(url, {
            method: 'GET',
            headers: {
                'Content-Type': 'application/json',
                'Authorization': `Bearer ${token}`,
            },
        });
        const json = await response.json();
        console.log(json)
    } catch (error) {
        console.error('Error:', error);
    }
}

api_calls();