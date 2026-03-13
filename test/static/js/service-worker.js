const CACHE_NAME = 'offline-cache-v1';
const urlsToCache = [
    '/',  
    '/dashboard',
    '/site',
    '/image-map',
    '/customer',
    '/userform',
    '/area',
    '/rows',
    '/tables',
    '/piles',
    '/assessment',
    '/remedy',
    '/inventory',
    '/invtrans',
    '/quality',
    '/reports',
    '/profile',
    '/user_log',
    '/comments',
    '/area1hotspot',
    '/area1remedyhotspot',
    '/updateusers',
    '/updatesite',
    '/updatecustomer',
    '/updateinventory',
    '/updateinvtrans',
    '/updatearea',
    '/updatetable',
    '/updatepile',
    '/updaterow',
    '/updateassmnt',
    '/updateremedy'
];

self.addEventListener('install', (event) => {
    event.waitUntil(
        caches.open(CACHE_NAME).then((cache) => {
            return cache.addAll(urlsToCache);
        })
    );
});

self.addEventListener('fetch', (event) => {
    event.respondWith(
        caches.match(event.request).then((response) => {
            return response || fetch(event.request);
        })
    );
});
