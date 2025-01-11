import { Component, inject } from '@angular/core';
import { ChatService } from '../services/chat.service';
import { FormsModule } from '@angular/forms';
import { HttpClientModule } from '@angular/common/http';

@Component({
  selector: 'app-chat',
  standalone: true,
  imports: [FormsModule, HttpClientModule],
  templateUrl: './chat.component.html',
  styleUrl: './chat.component.scss'
})
export class ChatComponent {
  chats: any[] = [];
  name: string = '';
  message: string = '';
  
  // chatService = inject(ChatService)
  constructor(private chatService: ChatService) { }

  ngOnInit() {
    this.getChats();
  }

  getChats() {
    this.chatService.getChats().subscribe(data => {
      this.chats = data;
    });
  }

  addChat() {
    if (this.name && this.message) {
      this.chatService.addChat(this.name, this.message).subscribe(() => {
        this.getChats();
      });
    }
  }
}
