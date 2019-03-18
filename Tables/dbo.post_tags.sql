CREATE TABLE [dbo].[post_tags]
(
[post_id] [int] NULL,
[tag_id] [int] NULL
) ON [PRIMARY]
GO
ALTER TABLE [dbo].[post_tags] ADD CONSTRAINT [FK__post_tags__post___2D27B809] FOREIGN KEY ([post_id]) REFERENCES [dbo].[post] ([id])
GO
ALTER TABLE [dbo].[post_tags] ADD CONSTRAINT [FK__post_tags__tag_i__2E1BDC42] FOREIGN KEY ([tag_id]) REFERENCES [dbo].[tag] ([id])
GO
