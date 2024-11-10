import { SidebarProvider, SidebarTrigger } from '@/components/ui/sidebar'
import { Outlet, useNavigation } from 'react-router-dom'
import AppSidebar from '@/components/app-sidebar'
import './root.css'

function Root() {
  const navigation = useNavigation()

  const loadingClass = navigation.state === 'loading' ? 'loading' : ''

  return (
    <SidebarProvider>
      <AppSidebar />
      <main className={`w-screen bg-merino ${loadingClass}`}>
        <SidebarTrigger />
        <Outlet />
      </main>
    </SidebarProvider>
  )
}

export default Root
