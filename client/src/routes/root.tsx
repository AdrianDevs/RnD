import { SidebarProvider, SidebarTrigger } from '@/components/ui/sidebar';
import { Outlet, useNavigation } from 'react-router-dom';
import AppSidebar from '@/components/app-sidebar';
import './root.css';

function Root() {
  const navigation = useNavigation();

  return (
    <SidebarProvider>
      <AppSidebar />
      <main className={navigation.state === 'loading' ? 'loading' : ''}>
        <SidebarTrigger />
        <Outlet />
      </main>
    </SidebarProvider>
  );
}

export default Root;
