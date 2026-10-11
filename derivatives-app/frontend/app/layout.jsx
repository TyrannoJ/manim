import "./globals.css";

export const metadata = {
  title: "My Website",
  description: "My Next.js website",
};

export default function RootLayout({ children }) {
  return (
    <html lang="en">
      <head>
        <meta charSet="UTF-8" name="viewport" content="width=device-width, initial-scale=1.0" />
        
      </head >
      <body className="bg-gray-900">
        {children}
      </body>
    </html>
  );
}