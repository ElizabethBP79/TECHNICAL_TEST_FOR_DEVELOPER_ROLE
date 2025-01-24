import { bootstrapApplication } from '@angular/platform-browser';
import { appConfig } from './app/app.config';
import { ImageProcessingComponent } from './app/image-processing.component';
import { importProvidersFrom } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { FileUploadModule } from 'primeng/fileupload';
import { CommonModule } from '@angular/common';
import { TableModule } from 'primeng/table';  


bootstrapApplication(ImageProcessingComponent, {
  providers: [
    importProvidersFrom(CommonModule),
    importProvidersFrom(FileUploadModule), // Agrega FileUploadModule aquí
    importProvidersFrom(TableModule),
  ],
}).catch((err) => console.error(err));