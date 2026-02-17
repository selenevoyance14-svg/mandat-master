import type { Metadata } from 'next'
import { Inter } from 'next/font/google'
import './globals.css'

const inter = Inter({ subsets: ['latin'] })

export const metadata: Metadata = {
    title: 'MandatMaster - Le Kit Ultime pour Agents Immobiliers',
    description: 'Obtenez plus de mandats avec nos templates, scripts et guides.',
}

export default function RootLayout({
    children,
}: {
    children: React.ReactNode
}) {
    return (
        <html lang="fr">
            <body className={inter.className}>{children}</body>
        </html>
    )
}
