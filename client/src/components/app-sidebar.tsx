import {
  Sidebar,
  SidebarContent,
  SidebarGroup,
  SidebarGroupContent,
  SidebarGroupLabel,
  SidebarHeader,
  SidebarMenu,
  SidebarMenuButton,
  SidebarMenuItem,
} from '@/components/ui/sidebar';
import { Survey } from '@/services/api';
import { Inbox } from 'lucide-react';
import { Link, useLoaderData } from 'react-router-dom';
import AppSidebarHeader from './app-sidebar-header';

function AppSidebar() {
  const surveys = useLoaderData() as Survey[];
  console.log('AppSidebar.surveys', surveys);

  return (
    <Sidebar>
      <SidebarHeader>
        <SidebarMenu>
          <SidebarMenuItem>
            <AppSidebarHeader />
          </SidebarMenuItem>
        </SidebarMenu>
      </SidebarHeader>
      <SidebarContent>
        <SidebarGroup>
          <SidebarGroupLabel>Leads</SidebarGroupLabel>
          <SidebarGroupContent>
            <SidebarMenu>
              {surveys.map((survey) => (
                <SidebarMenuItem key={survey.id}>
                  <SidebarMenuButton asChild>
                    <Link to={`surveys/${survey.id}`}>
                      <Inbox />
                      <span>{survey.name}</span>
                    </Link>
                  </SidebarMenuButton>
                </SidebarMenuItem>
              ))}
            </SidebarMenu>
          </SidebarGroupContent>
        </SidebarGroup>
      </SidebarContent>
    </Sidebar>
  );
}

export default AppSidebar;
