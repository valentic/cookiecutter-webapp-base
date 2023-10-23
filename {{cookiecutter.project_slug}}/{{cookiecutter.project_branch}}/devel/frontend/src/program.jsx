import React from 'react'
import { StoreProvider } from 'easy-peasy'
import { BrowserRouter } from 'react-router-dom'
import { MantineProvider } from '@mantine/core'
import { ModalsProvider } from '@mantine/modals'
import { Notifications } from '@mantine/notifications'
import { QueryClientProvider, QueryClient } from '@tanstack/react-query'

import { MultiProvider } from '~/support/helpers'

import { store } from '~/store'
import { App, AuthProvider } from '~/app'

const Program = () => {

    const queryClient = new QueryClient()

    const providers = [
        <React.StrictMode />,
        <StoreProvider store={store} />,
        <BrowserRouter basename={import.meta.env.VITE_ROOT_URL} />,
        <MantineProvider />,
        <ModalsProvider />,
        <QueryClientProvider client={queryClient} />,
        <AuthProvider />
    ]

    return (
      <MultiProvider providers={providers}>
        <Notifications />
        <App />
      </MultiProvider>
    )
}

export { Program }
