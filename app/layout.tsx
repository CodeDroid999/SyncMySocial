import './globals.css'
import { Inter } from 'next/font/google'

const inter = Inter({ subsets: ['latin'] })

export const metadata = {
  title: "SyncMySocial",
  description: 'SyncMySocial is a powerful open-source solution for managing all your social media accounts in one place. With seamless integration with popular social platforms, it simplifies the way you schedule posts, analyze engagement, and interact with your audience.',
}

export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <html lang="en">
      <body className={inter.className}>{children}</body>
    </html>
  )
}
