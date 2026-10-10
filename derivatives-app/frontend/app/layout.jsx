import "./globals.css";

export const metadata = {
  title: "My Website",
  description: "My Next.js website",
};

export default function RootLayout({ children }) {
  return (
    <html lang="en">
      <body>{children}</body>
    </html>
  );
}