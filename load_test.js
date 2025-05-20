import http from 'k6/http';
import { check, sleep } from 'k6';

export let options = {
  stages: [
    { duration: '1m', target: 50 }, // ramp-up to 50 virtual users over 1 minute
    { duration: '3m', target: 50 }, // stay at 50 users for 3 minutes
    { duration: '1m', target: 0 },  // ramp-down to 0 users
  ],
  thresholds: {
    http_req_duration: ['p(95)<500'], // 95% of requests below 500ms
    http_req_failed: ['rate<0.01'],    // <1% errors
  },
};

export default function () {
  let res = http.get('http://localhost:8080/');
  check(res, {
    'status is 200': (r) => r.status === 200,
    'response body non-empty': (r) => r.body.length > 0,
  });
  sleep(1);
}